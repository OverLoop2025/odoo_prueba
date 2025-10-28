odoo.define('exam_pos.zero_price_alert', function (require) {
    'use strict';

    const Registries = require('point_of_sale.Registries');
    const ProductScreen = require('point_of_sale.ProductScreen');

    const ZeroPriceProductScreen = (ProductScreen) => class extends ProductScreen {
        async _clickProduct(event) {
            const product = event.detail;
            const order = this.currentOrder;
            let price = 0;

            if (order) {
                const pricelist = order.pricelist;
                if (pricelist && typeof product.get_price === 'function') {
                    price = product.get_price(pricelist, 1);
                } else if (typeof order.get_product_price === 'function') {
                    price = order.get_product_price(product, 1);
                } else {
                    price = product.lst_price || 0;
                }
            }

            if (!price || Number(price) === 0) {
                await this.showPopup('ErrorPopup', {
                    title: this.env._t('Precio no permitido'),
                    body: this.env._t('Este producto tiene precio 0.0'),
                });
                return;
            }

            return super._clickProduct(event);
        }
    };

    Registries.Component.extend(ProductScreen, ZeroPriceProductScreen);
});
