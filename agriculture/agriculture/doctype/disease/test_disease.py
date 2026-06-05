# Copyright (c) 2017, Frappe Technologies Pvt. Ltd. and Contributors
# See license.txt

import frappe
from frappe.tests.utils import FrappeTestCase


class TestDisease(FrappeTestCase):
	def test_treatment_period(self):
		disease = frappe.get_doc('Disease', 'Aphids')
		self.assertEqual(disease.treatment_period, 3)
