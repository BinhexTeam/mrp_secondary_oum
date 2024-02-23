# -*- coding: utf-8 -*-

from odoo import api, fields, models
from odoo.tools.float_utils import float_round
import logging
_logger = logging.getLogger(__name__)

class StockMove(models.Model):
    _inherit = "stock.move"
    
    @api.onchange("secondary_uom_id", "quantity_done")
    def _compute_qty_done(self):
        for rec in self:
            if not rec.secondary_uom_id:
                continue
            if rec.secondary_uom_id.dependency_type == "independent":
                if rec[rec._secondary_unit_fields["qty_field"]] == 0.0:
                    rec[rec._secondary_unit_fields["qty_field"]] = 1.0
                continue
            # To avoid recompute secondary_uom_qty field when
            # secondary_uom_id changes.
            factor = rec._get_factor_line()
            qty = float_round(
                rec.secondary_uom_qty * factor,
                precision_rounding=rec._get_uom_line().rounding,
            )
            rec['secondary_uom_qty'] = qty
           
    def _quantity_done_compute(self):
        for move in self:
            temp_qty_done = move.quantity_done
            super(StockMove,move)._quantity_done_compute()
            if move.secondary_uom_id:
                move.quantity_done = temp_qty_done
    
    def action_refresh_secondary_unit(self):
        if self.product_id.purchase_secondary_uom_id:
            self.write({
                    'secondary_uom_id' : self.product_id.purchase_secondary_uom_id.id,
                })
        else:
            if self.product_id.secondary_uom_ids:
                self.write({
                        'secondary_uom_id' : self.product_id.secondary_uom_ids[0].id,
                    })
                