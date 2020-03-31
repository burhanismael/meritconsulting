# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from datetime import datetime
from uuid import uuid4

from odoo import api, fields, models, _
from odoo.exceptions import ValidationError




class PosConfig(models.Model):
    _inherit = 'pos.config'
    _description = 'Point of Sale Configuration'



    pos_credit = fields.Boolean(string='POS Credit Sale', help="Enable Credit Sale for this session.")
    
    

    
