odoo.define('exam_pos.boleta_button', function (require) {
    'use strict';
    const Registries = require('point_of_sale.Registries');
    const PaymentScreen = require('point_of_sale.PaymentScreen');

    const BoletaPaymentScreen = (PaymentScreen) => class extends PaymentScreen {
        get totalToPay() {
            return this.currentOrder ? this.currentOrder.get_total_with_tax() : 0;
        }
        async onClickBoleta() {
            await this.showPopup('ConfirmPopup', {
                title: this.env._t('Boleta'),
                body: this.env._t(`Total a pagar: ${this.env.pos.format_currency(this.totalToPay)}`),
                confirmText: this.env._t('OK'),
                cancelText: this.env._t('Cerrar'),
            });
        }
    };
    Registries.Component.extend(PaymentScreen, BoletaPaymentScreen);
});
