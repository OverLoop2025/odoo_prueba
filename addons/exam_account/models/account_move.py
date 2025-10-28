from odoo import models, fields, api, _
from odoo.exceptions import UserError
import io, base64

try:
    import qrcode
except Exception:
    qrcode = None

class ExamSaleChannel(models.Model):
    _name = "exam.sale.channel"
    _description = "Canal de Ventas (Exam)"
    name = fields.Char(required=True)


class AccountMove(models.Model):
    _inherit = "account.move"

    x_qr_invoice = fields.Binary(string="QR de Factura", readonly=True, attachment=True)
    x_total_qty = fields.Float(string="Total Cantidades", compute="_compute_total_qty", store=True)
    x_series = fields.Char(string="Número de serie", compute="_compute_series_correlative", store=True)
    x_correlative = fields.Char(string="Número correlativo", compute="_compute_series_correlative", store=True)
    x_sale_channel_id = fields.Many2one("exam.sale.channel", string="Canal de ventas")
    x_issue_datetime = fields.Datetime(string="Fecha de emisión")
    x_pickings = fields.Many2many("stock.picking", string="Transferencias relacionadas", compute="_compute_pickings", store=False)

    @api.depends("invoice_line_ids.quantity")
    def _compute_total_qty(self):
        for move in self:
            move.x_total_qty = sum(move.invoice_line_ids.mapped("quantity"))

    @api.depends("name")
    def _compute_series_correlative(self):
        for move in self:
            series = ""
            corr = ""
            if move.name and "/" in move.name:
                parts = move.name.split("/")
                if len(parts) >= 3:
                    series = f"{parts[0]}{parts[1]}"
                    corr = parts[2].zfill(8)
            move.update({"x_series": series, "x_correlative": corr})

    def _compute_pickings(self):
        for move in self:
            sale_orders = move.mapped("invoice_line_ids.sale_line_ids.order_id")
            pickings = sale_orders.mapped("picking_ids")
            move.x_pickings = [(6, 0, pickings.ids)]
    def generate_qr_code(self, qr_string):
        if qrcode is None:
            raise UserError(_("La librería 'qrcode' no está instalada en la imagen de Odoo."))
        qr = qrcode.QRCode(version=4, box_size=4, border=1)
        qr.add_data(qr_string)
        qr.make(fit=True)
        img = qr.make_image()
        buffer = io.BytesIO()
        img.save(buffer, format="PNG")
        img_str = base64.b64encode(buffer.getvalue())
        return {'x_qr_invoice': img_str}

    def action_generate_qr(self):
        for move in self:
            cliente = move.partner_id.display_name or ""
            fecha = (move.x_issue_datetime or move.invoice_date or fields.Datetime.now()).strftime("%Y-%m-%d %H:%M:%S") if hasattr(move, "x_issue_datetime") else str(move.invoice_date or "")
            total_qty = move.x_total_qty or 0.0
            total = move.amount_total or 0.0
            qr_str = f"{move.name}|{cliente}|{fecha}|{total_qty}|{total}"
            vals = move.generate_qr_code(qr_str)
            move.write(vals)
        return True
