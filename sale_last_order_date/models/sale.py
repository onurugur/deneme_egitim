




from odoo import models,fields,api
from odoo.exceptions import UserError




class SaleOrder(models.Model):
    _inherit='sale.order'




    sale_last_order_date = fields.Date('Sale Order Date',default='2024-01-01')


    @api.onchange('sale_last_order_date')
    def _onchange_sale_last_order_date(self):
        if self.sale_last_order_date:
            if self.sale_last_order_date > fields.datetime.today().date():
                raise UserError('Tarih ileri bir tarih olamaz')