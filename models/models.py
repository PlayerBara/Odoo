# -*- coding: utf-8 -*-

from odoo import models, fields, api
from dateutil.relativedelta import *
from datetime import date 

class pelicula(models.Model):
	_name = 'videoclub.pelicula'
	_description = 'Pelicula'

	name = fields.Char('Codigo pelicula',required=True)
	nombre = fields.Char(string='Pelicula',required=True)
	director = fields.Char(String='Director',required=True)
	fecha_salida = fields.Date(string='Fecha de salida',required=True)
	precio = fields.Integer("Precio",required=True)

	alquiler_peliculas_ids = fields.Many2one('videoclub.cliente' ,string='Cliente')

class cliente(models.Model):
	_name = 'videoclub.cliente'
	_description = 'Cliente'

	name = fields.Char("Codigo cliente", required=True)
	nombre = fields.Char(string='Nombre',required=True)
	telefono = fields.Char(string='Telefono',required=True)
	peliculas_ids = fields.One2many('videoclub.pelicula','alquiler_peliculas_ids',string='Cliente_pelicula')




# class videoclub(models.Model):
#     _name = 'videoclub.videoclub'
#     _description = 'videoclub.videoclub'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
