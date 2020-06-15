# Copyright 2017 Grant Thornton Spain - Ismael Calvo <ismael.calvo@es.gt.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import _, api, fields, models
from odoo.exceptions import ValidationError
from odoo.tools import config


class ResPartner(models.Model):
    _inherit = 'res.partner'

    vat = fields.Char(copy=False)

    @api.constrains('vat', 'main_id_number')
    def _check_vat_unique(self):
        for record in self:
            if record.parent_id or not record.vat:
                continue
            test_condition = (config['test_enable'] and
                              not self.env.context.get('test_vat'))
            if test_condition:
                continue
            results = self.env['res.partner'].search_count([
                ('main_id_number', '=', record.main_id_number),
                ('vat', '=', record.vat),
                ('main_id_number', 'not in', ['1-9', '00000001-9', '00000000-0', '55555555-5', '66666666-6']),
                ('id', '!=', record.id),
                ('parent_id', '=', False)
            ])
            if results:
                raise ValidationError(_(
                    "The VAT %s already exists in another "
                    "partner.") % record.main_id_number)
