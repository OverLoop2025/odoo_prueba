odoo.define('exam_pos.partner_lang', function (require) {
    'use strict';

    const Registries = require('point_of_sale.Registries');
    const { PosGlobalState } = require('point_of_sale.models');

    const PosGlobalStateExtend = (PosGlobalState) => class extends PosGlobalState {
        async setup() {
            await super.setup();
            console.log('[exam_pos] partner_lang.js cargado, models:', this.models);
            const partnerModel = (this.models || []).find((m) => m.model === 'res.partner');
            if (partnerModel) {
                partnerModel.fields = partnerModel.fields || [];
                if (!partnerModel.fields.includes('lang')) {
                    partnerModel.fields.push('lang');
                }
            }
        }
    };

    Registries.Model.extend(PosGlobalState, PosGlobalStateExtend);
});
