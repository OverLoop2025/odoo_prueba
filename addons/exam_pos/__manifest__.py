{
    "name": "Exam POS",
    "version": "16.0.1.0.0",
    "summary": "POS: columna Idioma en clientes, alerta precio 0.0, botón Boleta en PaymentScreen.",
    "author": "OverLoop - Jose",
    "license": "LGPL-3",
    "category": "Point of Sale",
    "depends": ["point_of_sale","contacts"],
    "data": [],
    "assets": {
        "point_of_sale.assets": [
            "exam_pos/static/src/js/zero_price_alert.js",
            "exam_pos/static/src/js/boleta_button.js",
            "exam_pos/static/src/js/partner_lang.js",
            "exam_pos/static/src/xml/boleta_button.xml",
            "exam_pos/static/src/xml/customer_lang.xml"
        ],
        "web.assets_qweb": [
            "exam_pos/static/src/xml/boleta_button.xml",
            "exam_pos/static/src/xml/customer_lang.xml"
        ]
    },
    "installable": True,
    "application": True
}
