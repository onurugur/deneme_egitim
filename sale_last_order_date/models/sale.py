




from odoo import models,fields,api
from odoo.exceptions import UserError




class SaleOrder(models.Model):
    _inherit='sale.order'




    sale_last_order_date = fields.Date('Sale Order Date',default='2024-01-01')

    sale_last_order_date_computed = fields.Date('Computed Sale Order Date',compute='_compute_sale_last_order_date_computed')


    @api.onchange('sale_last_order_date')
    def _onchange_sale_last_order_date(self):
        if self.sale_last_order_date:
            if self.sale_last_order_date > fields.datetime.today().date():
                raise UserError('Tarih ileri bir tarih olamaz')


    def _compute_sale_last_order_date_computed(self):
        sale_obj = self.env['sale.order']
        for sale in self:
            partner_id = sale.partner_id
            sale_orders = sale_obj.search([('state','in',['done','sale']),('partner_id','=',partner_id.id),('date_order','<',sale.date_order)])
            if sale_orders:
                sorted_sale_orders = sale_orders.sorted('date_order',reverse=True)
                sale.sale_last_order_date_computed = sorted_sale_orders[0].date_order
            else:
                sale.sale_last_order_date_computed = False
