# Copyright (c) 2017, Frappe Technologies Pvt. Ltd. and Contributors
# See license.txt

import frappe
from frappe.tests.utils import FrappeTestCase


class TestFertilizer(FrappeTestCase):
	def test_fertilizer_creation(self):
		self.assertEqual(frappe.db.exists('Fertilizer', 'Urea'), 'Urea')
