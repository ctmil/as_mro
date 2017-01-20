# -*- coding: utf-8 -*-

from openerp import models, fields, api, _
from openerp.osv import osv
from openerp.exceptions import except_orm, ValidationError
from StringIO import StringIO
import urllib2, httplib, urlparse, gzip, requests, json
import openerp.addons.decimal_precision as dp
import logging
import datetime
from openerp.fields import Date as newdate

#Get the logger
_logger = logging.getLogger(__name__)

"""
class as_expediente(models.Model):
	_name = 'as.expediente'
	_description = 'AS Expediente'
	_inherit = ['mail.thread']

	name = fields.Char('Nombre',required=True,track_visibility=True)
	date = fields.Date('Fecha',track_visibility=True)
	date_deadline = fields.Date('Fecha Vencimiento',track_visibility=True)
	contact_ids = fields.Many2many('res.partner', string='Contactos',track_visibility=True)
"""
