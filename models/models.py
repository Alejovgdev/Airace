# -*- coding: utf-8 -*-
from dataclasses import field


from odoo import models, fields, api


class player(models.Model):
     _name = 'airace.player'
     _description = 'airace.player'

     name = fields.Char(string="Nombre", readonly=False, required=True, help='Este es el nombre')
     coins = fields.Integer("Monedas")
     description = fields.Text()
     airplane_ids = fields.One2many('airace.airplane', 'player_id', string="Aviones")



class airplane(models.Model):
     _name = 'airace.airplane'
     _description = 'airace.airplane'

     name = fields.Char(string="Nombre", required=True, help='Este es el avion')
     speed = fields.Integer("Velocidad")
     maneuverability = fields.Integer("Maniobrabilidad")
     endurance = fields.Integer("Resistencia")
     fuel = fields.Float("Combustible")
     price = fields.Integer("Precio")
     description = fields.Text()
     player_id = fields.Many2one('airace.player', 'airplane_ids')





