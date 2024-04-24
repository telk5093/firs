from industry import IndustrySecondary, TileLocationChecks

industry = IndustrySecondary(
    id="tracked_machine_factory",
    accept_cargos_with_input_ratios=[
        ("VPTS", 2),
        ("VENG", 1),
        ("STSE", 3),
        ("PUMP", 1),
        ("WELD", 1),
    ],
    prod_cargo_types_with_output_ratios=[
        # high output production is unwanted
        ("VEHI", 2),
        ("FMSP", 2),
        ("ENSP", 2),
    ],
    prob_in_game="3",
    prob_map_gen="5",
    map_colour="49",
    name="string(STR_IND_TRACKED_MACHINE_FACTORY)",
    nearby_station_name="string(STR_STATION_TRACKED_MACHINE_FACTORY)",
    fund_cost_multiplier="145",
    sprites_complete=False,
)

industry.enable_in_economy(
    "STEELTOWN",
)

industry.add_tile(
    id="tracked_machine_factory_tile_1",
    animation_length=71,
    animation_looping=True,
    animation_speed=2,
    location_checks=TileLocationChecks(
        require_effectively_flat=True, disallow_industry_adjacent=True
    ),
)

spriteset_ground = industry.add_spriteset(
    type="asphalt",
)
spriteset_ground_overlay = industry.add_spriteset(type="empty")
spriteset_1 = industry.add_spriteset(
    sprites=[(10, 10, 64, 31, -31, 0)],
)
spriteset_2 = industry.add_spriteset(
    sprites=[(80, 10, 64, 31, -31, 0)],
)
spriteset_3 = industry.add_spriteset(
    sprites=[(150, 10, 64, 78, -25, -12)],
)
spriteset_4 = industry.add_spriteset(
    sprites=[(220, 10, 64, 78, -48, -28)],
)
spriteset_5 = industry.add_spriteset(
    sprites=[(290, 10, 64, 78, -31, -47)],
)
spriteset_6 = industry.add_spriteset(
    sprites=[(360, 10, 64, 78, -31, -47)],
)
spriteset_7 = industry.add_spriteset(
    sprites=[(430, 10, 64, 78, -31, -47)],
)
spriteset_8 = industry.add_spriteset(
    sprites=[(500, 10, 64, 85, -31, -54)],
)
spriteset_9 = industry.add_spriteset(
    sprites=[(570, 10, 64, 85, -31, -54)],
)
spriteset_10 = industry.add_spriteset(
    sprites=[(640, 10, 64, 85, -31, -54)],
)
spriteset_11 = industry.add_spriteset(
    sprites=[(780, 10, 64, 31, -35, 2)],
)
spriteset_12 = industry.add_spriteset(
    sprites=[(850, 10, 64, 31, -35, 2)],
)
spriteset_13 = industry.add_spriteset(
    sprites=[(920, 10, 64, 49, -39, -15)],
)
# out of sequence for historical reasons
spriteset_14 = industry.add_spriteset(
    sprites=[(710, 10, 64, 31, -28, -1)],
)
sprite_smoke = industry.add_smoke_sprite(
    smoke_type="dark_smoke_small",
    xoffset=13,
    yoffset=0,
    zoffset=73,
)

industry.add_spritelayout(
    id="tracked_machine_factory_spritelayout_1",
    tile="tracked_machine_factory_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_1],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="tracked_machine_factory_spritelayout_2",
    tile="tracked_machine_factory_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_2],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="tracked_machine_factory_spritelayout_3",
    tile="tracked_machine_factory_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_3],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="tracked_machine_factory_spritelayout_4",
    tile="tracked_machine_factory_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_4],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="tracked_machine_factory_spritelayout_5",
    tile="tracked_machine_factory_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_5],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="tracked_machine_factory_spritelayout_6",
    tile="tracked_machine_factory_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    # building_sprites = [spriteset_6, spriteset_14], # commented due to spritesorter issues obscuring spriteset_14
    building_sprites=[spriteset_6],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="tracked_machine_factory_spritelayout_7",
    tile="tracked_machine_factory_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_7],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="tracked_machine_factory_spritelayout_8",
    tile="tracked_machine_factory_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_8],
    smoke_sprites=[sprite_smoke],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="tracked_machine_factory_spritelayout_9",
    tile="tracked_machine_factory_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_9],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="tracked_machine_factory_spritelayout_10",
    tile="tracked_machine_factory_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_10],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="tracked_machine_factory_spritelayout_11",
    tile="tracked_machine_factory_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_11],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="tracked_machine_factory_spritelayout_12",
    tile="tracked_machine_factory_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_12],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="tracked_machine_factory_spritelayout_13",
    tile="tracked_machine_factory_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_13],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="tracked_machine_factory_spritelayout_14",
    tile="tracked_machine_factory_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[],
    fences=["nw", "ne", "se", "sw"],
)


industry.add_industry_layout(
    id="tracked_machine_factory_industry_layout_1",
    layout=[
        (0, 0, "tracked_machine_factory_spritelayout_2"),
        (0, 1, "tracked_machine_factory_spritelayout_7"),
        (0, 2, "tracked_machine_factory_spritelayout_14"),
        (1, 0, "tracked_machine_factory_spritelayout_6"),
        (1, 1, "tracked_machine_factory_spritelayout_5"),
        (1, 2, "tracked_machine_factory_spritelayout_13"),
        (2, 0, "tracked_machine_factory_spritelayout_2"),
        (2, 1, "tracked_machine_factory_spritelayout_10"),
        (2, 2, "tracked_machine_factory_spritelayout_12"),
        (3, 0, "tracked_machine_factory_spritelayout_9"),
        (3, 1, "tracked_machine_factory_spritelayout_8"),
        (3, 2, "tracked_machine_factory_spritelayout_11"),
        (4, 0, "tracked_machine_factory_spritelayout_3"),
        (4, 1, "tracked_machine_factory_spritelayout_4"),
        (4, 2, "tracked_machine_factory_spritelayout_13"),
        (5, 0, "tracked_machine_factory_spritelayout_2"),
        (5, 1, "tracked_machine_factory_spritelayout_1"),
        (5, 2, "tracked_machine_factory_spritelayout_2"),
    ],
)
industry.add_industry_layout(
    id="tracked_machine_factory_industry_layout_2",
    layout=[
        (0, 0, "tracked_machine_factory_spritelayout_1"),
        (0, 1, "tracked_machine_factory_spritelayout_7"),
        (0, 2, "tracked_machine_factory_spritelayout_1"),
        (0, 3, "tracked_machine_factory_spritelayout_7"),
        (0, 4, "tracked_machine_factory_spritelayout_12"),
        (1, 0, "tracked_machine_factory_spritelayout_6"),
        (1, 1, "tracked_machine_factory_spritelayout_5"),
        (1, 2, "tracked_machine_factory_spritelayout_6"),
        (1, 3, "tracked_machine_factory_spritelayout_5"),
        (1, 4, "tracked_machine_factory_spritelayout_11"),
        (2, 0, "tracked_machine_factory_spritelayout_1"),
        (2, 1, "tracked_machine_factory_spritelayout_10"),
        (2, 2, "tracked_machine_factory_spritelayout_14"),
        (2, 3, "tracked_machine_factory_spritelayout_3"),
        (2, 4, "tracked_machine_factory_spritelayout_4"),
        (3, 0, "tracked_machine_factory_spritelayout_9"),
        (3, 1, "tracked_machine_factory_spritelayout_8"),
        (3, 2, "tracked_machine_factory_spritelayout_13"),
        (3, 3, "tracked_machine_factory_spritelayout_2"),
        (3, 4, "tracked_machine_factory_spritelayout_1"),
    ],
)
industry.add_industry_layout(
    id="tracked_machine_factory_industry_layout_3",
    layout=[
        (0, 0, "tracked_machine_factory_spritelayout_1"),
        (0, 1, "tracked_machine_factory_spritelayout_7"),
        (0, 2, "tracked_machine_factory_spritelayout_1"),
        (0, 3, "tracked_machine_factory_spritelayout_7"),
        (0, 4, "tracked_machine_factory_spritelayout_14"),
        (1, 0, "tracked_machine_factory_spritelayout_6"),
        (1, 1, "tracked_machine_factory_spritelayout_5"),
        (1, 2, "tracked_machine_factory_spritelayout_6"),
        (1, 3, "tracked_machine_factory_spritelayout_5"),
        (1, 4, "tracked_machine_factory_spritelayout_12"),
        (2, 0, "tracked_machine_factory_spritelayout_3"),
        (2, 1, "tracked_machine_factory_spritelayout_4"),
        (2, 2, "tracked_machine_factory_spritelayout_1"),
        (2, 3, "tracked_machine_factory_spritelayout_10"),
        (2, 4, "tracked_machine_factory_spritelayout_11"),
        (3, 0, "tracked_machine_factory_spritelayout_2"),
        (3, 1, "tracked_machine_factory_spritelayout_1"),
        (3, 2, "tracked_machine_factory_spritelayout_9"),
        (3, 3, "tracked_machine_factory_spritelayout_8"),
        (3, 4, "tracked_machine_factory_spritelayout_13"),
    ],
)
industry.add_industry_layout(
    id="tracked_machine_factory_industry_layout_4",
    layout=[
        (0, 0, "tracked_machine_factory_spritelayout_1"),
        (0, 1, "tracked_machine_factory_spritelayout_7"),
        (0, 2, "tracked_machine_factory_spritelayout_13"),
        (0, 3, "tracked_machine_factory_spritelayout_3"),
        (0, 4, "tracked_machine_factory_spritelayout_4"),
        (1, 0, "tracked_machine_factory_spritelayout_6"),
        (1, 1, "tracked_machine_factory_spritelayout_5"),
        (1, 2, "tracked_machine_factory_spritelayout_2"),
        (1, 3, "tracked_machine_factory_spritelayout_1"),
        (1, 4, "tracked_machine_factory_spritelayout_12"),
        (2, 0, "tracked_machine_factory_spritelayout_1"),
        (2, 1, "tracked_machine_factory_spritelayout_7"),
        (2, 2, "tracked_machine_factory_spritelayout_1"),
        (2, 3, "tracked_machine_factory_spritelayout_10"),
        (2, 4, "tracked_machine_factory_spritelayout_11"),
        (3, 0, "tracked_machine_factory_spritelayout_6"),
        (3, 1, "tracked_machine_factory_spritelayout_5"),
        (3, 2, "tracked_machine_factory_spritelayout_9"),
        (3, 3, "tracked_machine_factory_spritelayout_8"),
        (3, 4, "tracked_machine_factory_spritelayout_13"),
    ],
)
industry.add_industry_layout(
    id="tracked_machine_factory_industry_layout_5",
    layout=[
        (0, 0, "tracked_machine_factory_spritelayout_3"),
        (0, 1, "tracked_machine_factory_spritelayout_4"),
        (0, 2, "tracked_machine_factory_spritelayout_1"),
        (0, 3, "tracked_machine_factory_spritelayout_7"),
        (0, 4, "tracked_machine_factory_spritelayout_1"),
        (0, 5, "tracked_machine_factory_spritelayout_10"),
        (1, 0, "tracked_machine_factory_spritelayout_12"),
        (1, 1, "tracked_machine_factory_spritelayout_11"),
        (1, 2, "tracked_machine_factory_spritelayout_6"),
        (1, 3, "tracked_machine_factory_spritelayout_5"),
        (1, 4, "tracked_machine_factory_spritelayout_9"),
        (1, 5, "tracked_machine_factory_spritelayout_8"),
        (2, 0, "tracked_machine_factory_spritelayout_13"),
        (2, 1, "tracked_machine_factory_spritelayout_13"),
        (2, 2, "tracked_machine_factory_spritelayout_14"),
        (2, 3, "tracked_machine_factory_spritelayout_2"),
        (2, 4, "tracked_machine_factory_spritelayout_1"),
        (2, 5, "tracked_machine_factory_spritelayout_1"),
    ],
)