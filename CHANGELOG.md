# Changelog

## Unreleased

- `chart_tooltip`'s `is_animation_active`, `separator`, `cursor`, `item_style`, `label_style`, and `content_style` parameters, and `high_level_table`'s (`table(...)`) `striped` parameter, are now keyword-only. Code that passed any of these positionally will raise `TypeError`; pass them by keyword instead (e.g. `chart_tooltip(is_animation_active=True)`, `table(data=..., striped=True)`).
- Removed the `LiteralCollisionAvoidance` alias from `components/ui/menu.py` and `components/ui/context_menu.py`; its values (`flip`/`shift`/`auto`) were never valid in Base UI, so imports of it will now raise `ImportError`. `collision_avoidance` on the menu, context menu, popover, and select positioners now accepts `str | dict[str, str]` (menu also accepts `bool`).
- Theme preset seeds now cover every registered font. Since the seed format has no version marker, some previously shared 9-character preset URLs may now resolve to a different theme; recreate and reshare affected presets.
