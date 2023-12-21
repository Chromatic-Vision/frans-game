def place(block):
    # if game.player.x > TILE_SIZE * 10:
    #     game.refresh_map('test2')
    if block.type == 5:
        def update():
            if game.player.x // TILE_SIZE == block.x \
                    and game.player.y // TILE_SIZE == block.y:
                game.player.x = 2 * TILE_SIZE
                game.player.y = 4 * TILE_SIZE

                if game.current_map_name == "test":
                    game.refresh_map('test2')
                elif game.current_map_name == "test2":
                        game.refresh_map('debug')
                elif game.current_map_name == "debug":
                        game.refresh_map('test')

        event(Event.UPDATE, update)


event(Event.PLACE, place)
