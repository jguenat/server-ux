# Copyright 2017-19 ForgeFlow S.L. (https://www.forgeflow.com)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
{
    "name": "Base Tier Validation",
    "summary": "Implement a validation process based on tiers.",
    "version": "16.0.1.3.1",
    "development_status": "Mature",
    "maintainers": ["LoisRForgeFlow"],
    "category": "Tools",
    "website": "https://github.com/OCA/server-ux",
    "author": "ForgeFlow, Odoo Community Association (OCA)",
    "license": "AGPL-3",
    "application": False,
    "installable": True,
    "depends": ["mail"],
    "data": [
        "data/mail_data.xml",
        "security/ir.model.access.csv",
        "security/tier_validation_security.xml",
        "views/res_config_settings_views.xml",
        "views/tier_definition_view.xml",
        "views/tier_review_view.xml",
        "wizard/comment_wizard_view.xml",
        "templates/tier_validation_templates.xml",
    ],
    "assets": {
        "web.assets_backend": [
            "/base_tier_validation/static/src/scss/systray.scss",
            "/base_tier_validation/static/src/scss/review.scss",
            "/base_tier_validation/static/src/js/main.esm.js",
            "/base_tier_validation/static/src/js/ir_model.esm.js",
            "/base_tier_validation/static/src/js/systray_service.esm.js",
            "/base_tier_validation/static/src/js/systray.esm.js",
            "/base_tier_validation/static/src/js/review_groups.esm.js",
            "/base_tier_validation/static/src/js/reviewer_menu_view.esm.js",
            "/base_tier_validation/static/src/js/tier_review_widget.esm.js",
            "/base_tier_validation/static/src/js/review_group_view.esm.js",
            "/base_tier_validation/static/src/js/reviewer_menu_container.esm.js",
            "/base_tier_validation/static/src/js/review_notification_handler.esm.js",
            "/base_tier_validation/static/src/xml/**/*",
        ],
    },
}
