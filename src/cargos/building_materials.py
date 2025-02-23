from cargo import Cargo

cargo = Cargo(
    id="building_materials",
    type_name="string(STR_CARGO_NAME_BUILDING_MATERIALS)",
    unit_name="string(STR_CARGO_NAME_BUILDING_MATERIALS)",
    type_abbreviation="string(STR_CID_BUILDING_MATERIALS)",
    sprite="NEW_CARGO_SPRITE",
    weight="1.0",
    is_freight="1",
    cargo_classes = ["CC_PIECE_GOODS", "CC_COVERED_BULK", "CC_FLATBED", "CC_NON_POTABLE"],
    cargo_label="BDMT",
    units_of_cargo="TTD_STR_TONS",
    items_of_cargo="string(STR_CARGO_UNIT_BUILDING_MATERIALS)",
    penalty_lowerbound="12",
    single_penalty_length="255",
    price_factor=133,
    capacity_multiplier="1",
    icon_indices=(1, 1),
    # used by FIRS GS
    vulcan_town_effect="VTE_GROWTH",
    sprites_complete=True,
)
