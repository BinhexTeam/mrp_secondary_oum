from odoo import fields, models, api

class MRPProduction(models.Model):
    _inherit="mrp.production"
    
    def action_refresh_secondary_unit_in_moves(self):
        for move in self.move_raw_ids:
            move.action_refresh_secondary_unit()
            
            
    
    
        
    