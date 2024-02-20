from odoo import fields,models,api,_


import logging
_logger = logging.getLogger(__name__)



class StockMove(models.Model):
    _inherit="stock.move"
    
    def action_refresh_secondary_unit(self):
    
        if self.product_id.secondary_uom_ids:
            self.write({
                    'secondary_uom_id' : self.product_id.secondary_uom_ids[0].id,
                    'secondary_uom_qty' : self.product_id.secondary_uom_ids[0].factor
                })
            
            