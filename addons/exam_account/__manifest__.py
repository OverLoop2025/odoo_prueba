{
    "name": "Exam Account",
    "version": "16.0.1.0.0",
    "summary": "Factura: QR, serie/correlativo, canal de ventas, fecha de emisión (datetime), pickings relacionados y reporte.",
    "author": "Jose - OverLoop",
    "license": "LGPL-3",
    "category": "Accounting/Accounting",
    "depends": ["account","sale_management","stock"],
    "data": [
        "security/ir.model.access.csv",
        "data/sale_channel_data.xml",
        "views/account_move_views.xml",
        "report/report_invoice_inherit.xml"
    ],
    "installable": True,
    "application": True
}
