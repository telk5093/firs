from cargo import Cargo

cargo = Cargo(
    id="edible_oil",
    type_name="string(STR_CARGO_NAME_EDIBLE_OIL)",
    unit_name="string(STR_CARGO_NAME_EDIBLE_OIL)",
    type_abbreviation="string(STR_CID_EDIBLE_OIL)",
    sprite="NEW_CARGO_SPRITE",
    weight="1.0",
    is_freight="1",
    cargo_classes = ["CC_PIECE_GOODS", "CC_LIQUID_BULK", "CC_POTABLE"],
    cargo_label="EOIL",
    units_of_cargo="TTD_STR_LITERS",
    items_of_cargo="string(STR_CARGO_UNIT_EDIBLE_OIL)",
    penalty_lowerbound="20",
    single_penalty_length="128",
    price_factor=116,
    capacity_multiplier="1",
    icon_indices=(0, 3),
    sprites_complete=True,
)
