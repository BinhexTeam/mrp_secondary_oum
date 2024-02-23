# -*- coding: utf-8 -*-

from odoo import api, fields, models, _

import logging
_logger = logging.getLogger(__name__)

class StockMove(models.Model):
    _inherit = "stock.move"
    
    custom_secondary_uom_id = fields.Many2one(
        string=_('Secondary unit'),
        comodel_name='product.secondary.unit'
    )
    custom_secondary_uom_qty = fields.Float(
        string=_('Secondary unit'),
        compute="_compute_custom_secondary_uom_qty",
        digits = (12,4)
        ) 
    
    @api.depends('custom_secondary_uom_id', 'product_uom_qty')
    def _compute_custom_secondary_uom_qty(self):
        for move in self:
            if not move.custom_secondary_uom_id:
                move.custom_secondary_uom_qty = 0
            else:
                move.custom_secondary_uom_qty = move.product_uom_qty * move.custom_secondary_uom_id.factor
    
    def action_refresh_secondary_unit(self):
        if self.product_id.purchase_secondary_uom_id:
            self.write({
                    'custom_secondary_uom_id' : self.product_id.purchase_secondary_uom_id.id,
                    'custom_secondary_uom_qty' : self.product_uom_qty * self.product_id.purchase_secondary_uom_id.factor
                })
        else:
            if self.product_id.secondary_uom_ids:
                self.write({
                        'custom_secondary_uom_id' : self.product_id.secondary_uom_ids[0].id,
                        'custom_secondary_uom_qty' : self.product_uom_qty * self.product_id.secondary_uom_ids[0].factor
                    })
                