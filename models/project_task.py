# -*- coding: utf-8 -*-
from odoo import models, fields

class ProjectTask(models.Model):
    _inherit = 'project.task'

    # Fecha de Inicio
    start_date = fields.Date(
        string='Fecha de Inicio',
        tracking=True,
        help='Fecha de inicio planificada de la tarea.'
    )

    # Orden de Compra (enlazar múltiples POs)
    purchase_order_ids = fields.Many2many(
        comodel_name='purchase.order',
        relation='task_purchase_order_rel',   # nombre de la tabla rel
        column1='task_id',
        column2='purchase_order_id',
        string='Orden de Compra',
        help='Órdenes de compra vinculadas a esta tarea.'
    )
