import setuptools

with open('VERSION.txt', 'r') as f:
    version = f.read().strip()

setuptools.setup(
    name="odoo10-addons-oca-partner-contact",
    description="Meta package for oca-partner-contact Odoo addons",
    version=version,
    install_requires=[
        'odoo10-addon-base_country_state_translatable',
        'odoo10-addon-base_location',
        'odoo10-addon-base_location_geonames_import',
        'odoo10-addon-base_location_nuts',
        'odoo10-addon-base_partner_merge',
        'odoo10-addon-base_partner_sequence',
        'odoo10-addon-base_vat_sanitized',
        'odoo10-addon-partner_academic_title',
        'odoo10-addon-partner_address_street3',
        'odoo10-addon-partner_affiliate',
        'odoo10-addon-partner_alias',
        'odoo10-addon-partner_bank_active',
        'odoo10-addon-partner_capital',
        'odoo10-addon-partner_changeset',
        'odoo10-addon-partner_coc',
        'odoo10-addon-partner_company_type',
        'odoo10-addon-partner_contact_birthdate',
        'odoo10-addon-partner_contact_birthplace',
        'odoo10-addon-partner_contact_configuration',
        'odoo10-addon-partner_contact_department',
        'odoo10-addon-partner_contact_gender',
        'odoo10-addon-partner_contact_in_several_companies',
        'odoo10-addon-partner_contact_job_position',
        'odoo10-addon-partner_contact_lang',
        'odoo10-addon-partner_contact_nationality',
        'odoo10-addon-partner_contact_nutrition',
        'odoo10-addon-partner_contact_nutrition_activity_level',
        'odoo10-addon-partner_contact_nutrition_goal',
        'odoo10-addon-partner_contact_personal_information_page',
        'odoo10-addon-partner_contact_role',
        'odoo10-addon-partner_contact_weight',
        'odoo10-addon-partner_create_by_vat',
        'odoo10-addon-partner_disable_gravatar',
        'odoo10-addon-partner_email_check',
        'odoo10-addon-partner_employee_quantity',
        'odoo10-addon-partner_external_map',
        'odoo10-addon-partner_financial_risk',
        'odoo10-addon-partner_firstname',
        'odoo10-addon-partner_helper',
        'odoo10-addon-partner_identification',
        'odoo10-addon-partner_label',
        'odoo10-addon-partner_multi_relation',
        'odoo10-addon-partner_password_reset',
        'odoo10-addon-partner_phone_extension',
        'odoo10-addon-partner_phonecall_schedule',
        'odoo10-addon-partner_risk_insurance',
        'odoo10-addon-partner_sale_risk',
        'odoo10-addon-partner_second_lastname',
        'odoo10-addon-partner_sector',
        'odoo10-addon-partner_stock_risk',
        'odoo10-addon-partner_street_number',
        'odoo10-addon-partner_vat_unique',
    ],
    classifiers=[
        'Programming Language :: Python',
        'Framework :: Odoo',
    ]
)
