from cargo import Cargo

cargo = Cargo(
    id="manganese",
    type_name="string(STR_CARGO_NAME_MANGANESE)",
    unit_name="string(STR_CARGO_NAME_MANGANESE)",
    type_abbreviation="string(STR_CID_MANGANESE)",
    sprite="NEW_CARGO_SPRITE",
    weight="1.0",
    is_freight="1",
    cargo_classes = ["CC_OPEN_BULK", "CC_NON_POTABLE"],
    cargo_label="MNO2",
    units_of_cargo="TTD_STR_TONS",
    items_of_cargo="string(STR_CARGO_UNIT_MANGANESE)",
    penalty_lowerbound="30",
    single_penalty_length="255",
    price_factor=95,
    capacity_multiplier="1",
    icon_indices=(9, 2),
    sprites_complete=True,
)
