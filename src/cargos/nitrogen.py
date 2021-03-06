from cargo import Cargo

cargo = Cargo(
    id="nitrogen",
    type_name="string(STR_CARGO_NAME_NITROGEN)",
    unit_name="string(STR_CARGO_NAME_NITROGEN)",
    type_abbreviation="string(STR_CID_NITROGEN)",
    sprite="NEW_CARGO_SPRITE",
    weight="1.0",
    is_freight="1",
    cargo_classes="bitmask(CC_LIQUID, CC_HAZARDOUS)",
    cargo_label="O2__",
    town_growth_effect="TOWNGROWTH_NONE",
    town_growth_multiplier="1.0",
    units_of_cargo="TTD_STR_LITERS",
    items_of_cargo="string(STR_CARGO_UNIT_NITROGEN)",
    penalty_lowerbound="22",
    single_penalty_length="44",
    price_factor=152,
    capacity_multiplier="1",
    icon_indices=(1, 5),
)
