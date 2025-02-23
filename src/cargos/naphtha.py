from cargo import Cargo

# the specific petrochemical feedstock rather than the generic term for petroleum spirits

cargo = Cargo(
    id="naphtha",
    type_name="string(STR_CARGO_NAME_NAPHTHA)",
    unit_name="string(STR_CARGO_NAME_NAPHTHA)",
    type_abbreviation="string(STR_CID_NAPHTHA)",
    sprite="NEW_CARGO_SPRITE",
    weight="0.8",
    is_freight="1",
    cargo_classes = ["CC_LIQUID_BULK", "CC_NON_POTABLE"],
    cargo_label="NAPH",
    units_of_cargo="TTD_STR_LITERS",
    items_of_cargo="string(STR_CARGO_UNIT_NAPHTHA)",
    penalty_lowerbound="18",
    single_penalty_length="255",
    capacity_multiplier="1",
    price_factor=103,
    icon_indices=(12, 1),
    sprites_complete=False,
)
