import frappe


def get_context(context):
	context.no_cache = 1
	batch_name = frappe.form_dict["batch"]
	context.batch = frappe.get_doc("LMS Batch Old", batch_name)
	context.already_a_member = context.batch.is_member(frappe.session.user)
	context.batch.course_title = frappe.db.get_value(
		"LMS Course", context.batch.course, "title"
	)
