# Copyright (C) 2021-Today: GRAP (http://www.grap.coop)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import fields, models


class ResCompany(models.Model):
    _inherit = "res.company"

    joint_buying_send_pivot_email_in_progress = fields.Boolean(
        string="Send email when opening Grouped Order", default=False
    )

    joint_buying_send_pivot_email_closed = fields.Boolean(
        "Send email when closing Grouped Order", default=True
    )
