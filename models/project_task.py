from odoo import models, fields

class ProjectTask(models.Model):
    _inherit = 'project.task'

    purchase_order_ids = fields.Many2many(
        'purchase.order',
        'task_purchase_order_rel',
        'task_id',
        'purchase_order_id',
        string='Orden de Compra'
    )

    start_date = fields.Date(
        string='Fecha de Inicio'
    )
