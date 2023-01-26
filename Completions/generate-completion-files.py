from __future__ import annotations
import dataclasses
import json
from pathlib import Path

completion_folder = Path(__file__).parent/'Completions/'

def json_dump(d, fname=None, sort_keys=False, indent=4, **kwds):
    if fname:
        with open(fname, 'w') as fp:
            json.dump(d, fp, sort_keys=sort_keys, indent=indent, **kwds)
    return json.dumps(d, sort_keys=sort_keys, indent=indent, **kwds)

@dataclasses.dataclass(slots=True)
class CompletionItem:
    trigger: str
    kind: str|(str, str, str)
    contents: str = ''
    annotation: str = ''
    details: str = ''

    def to_dict(self):
        d = {'trigger': self.trigger}
        if self.contents:
            d['contents'] = self.contents
        if self.annotation:
            d['annotation'] = self.annotation
        d['kind'] = self.kind
        if self.details:
            d['details'] = self.details
        return d

class CompletionList:
    def __init__(self, items:list[CompletionItem|str]=[], fname:Path|str|None=None, *, scope:str='source.scarpet', default_style:dict={}):
        self.scope: str = 'source.scarpet'
        self._items: list[CompletionItem] = []
        self.default_style: dict = default_style

        for item in items:
            if isinstance(item, str):
                item = CompletionItem(item, **self.default_style)
            self._items.append(item)

        if fname is not None and not isinstance(fname, Path):
            fname = Path(fname)
        self._fname:Path|None = fname

    @property
    def fname(self):
        return self._fname

    @property
    def items(self):
        return self._items


    def __getitem__(self, key:str) -> CompletionItem:
        items = filter(lambda item: item.trigger == key, self._items)
        try:
            return next(items)
        except StopIteration:
            raise KeyError(key)

    def to_dict(self) -> dict:
        d = {'scope': self.scope, 'completions': [item.to_dict() for item in self._items]}
        return d

    def combine(self, *y:CompletionList, fname:Path|str|None=None, scope:str='source.scarpet', default_style:dict={}):
        for _y in y:
            self._items.extend(_y._items)

    @staticmethod
    def combined(*x:CompletionList, fname:Path|str|None=None, scope:str='source.scarpet', default_style:dict={}) -> CompletionList:
        '''Combine two `CompletionList`
        All `CompletionList` are combined to one.
        The combined `CompletionList` will inherits the `scope` and `default_style` of the first `CompletionList`

        Args:
            x (Tuple[CompletionList]): The `CompletionList` to be combined
        '''
        cl = CompletionList(scope=scope, default_style=default_style)
        if not x:
            return cl
        cl.scope = x[0].scope
        cl.default_style = x[0].default_style
        if fname is None:
            fname = x[0]._fname
        cl._fname = fname
        for _x in x:
            cl.combine(_x)
        return cl

    def to_json(self, fname=None):
        if fname is None:
            fname=self._fname
        d = self.to_dict()
        ret = json_dump(d, fname)
        if fname:
            return ret

function_table = {
'variables': {
 '_',
 '_a',
 '_i',
 '_x',
 '_y',
 '_z',
 '_trace'
},
'constants': {
 'null',
 'true',
 'false',
 'pi',
 'euler',
 },

'operators': {
 'and()',
 'decreasing()',
 'delete()',
 'difference()',
 'equal()',
 'get()',
 'has()',
 'increasing()',
 'nondecreasing()',
 'nonincreasing()',
 'not()',
 'or()',
 'product()',
 'put()',
 'quotient()',
 'sum()',
 'unique()',
 'bitwise_and()',
 'bitwise_xor()',
 'bitwise_or()',
 'bitwise_shift_left()',
 'bitwise_shift_right()',
 'bitwise_roll_left()',
 'bitwise_roll_right()',
 'bitwise_not()',
 'bitwise_popcount()',
 'double_to_long_bits()',
 'long_bits_to_double()',
 'long_to_double_bits()',
 '...',
 '->'
 },

'mathematical_functions': {
 'abs()',
 'acos()',
 'acosh()',
 'acot()',
 'asin()',
 'asinh()',
 'atan()',
 'atan2()',
 'atanh()',
 'ceil()',
 'cos()',
 'cosh()',
 'cot()',
 'coth()',
 'csc()',
 'csch()',
 'deg()',
 'fact()',
 'floor()',
 'ln()',
 'ln1p()',
 'log()',
 'log10()',
 'log1p()',
 'mandelbrot()',
 'max()',
 'min()',
 'rad()',
 'relu()',
 'round()',
 'sec()',
 'sech()',
 'sin()',
 'sinh()',
 'sqrt()',
 'tan()',
 'tanh()'
 },

'system_functions': {
 'bool()',
 'convert_date()',
 'copy()',
 'decode_b64()',
 'decode_json()',
 'encode_b64()',
 'encode_json()',
 'hash_code()',
 'length()',
 'lower()',
 'number()',
 'perlin()',
 'print()',
 'profile_expr()',
 'rand()',
 'replace()',
 'replace_first()',
 'simplex()',
 'sleep()',
 'str()',
 'synchronize()',
 'system_variable_get()',
 'system_variable_set()',
 'task()',
 'task_completed()',
 'task_count()',
 'task_dock()',
 'task_join()',
 'task_thread()',
 'task_value()',
 'time()',
 'title()',
 'type()',
 'undef()',
 'unix_time()',
 'upper()',
 'var()',
 'vars()'
 },

'loops_and_higher_order_functions': {
 'all()',
 'break()',
 'c_for()',
 'continue()',
 'filter()',
 'first()',
 'for()',
 'loop()',
 'map()',
 'reduce()',
 'while()'
},

'user_defined_functions_and_program_control_flow': {
 'try()',
 'return()',
 'import()',
 'call()',
 'throw()',
 'if()',
 'then()',
 'exit()',
 'outer()'
 },

'container_types': {
 'delete()',
 'get()',
 'has()',
 'join()',
 'keys()',
 'l()',
 'm()',
 'pairs()',
 'put()',
 'range()',
 'slice()',
 'sort()',
 'sort_key()',
 'split()',
 'values()'},

'app': {
 '__config()',
},

'blocks_and_world_access': {
 'add_chunk_ticket()',
 'air()',
 'biome()',
 'blast_resistance()',
 'block()',
 'block_data()',
 'block_light()',
 'block_list()',
 'block_properties()',
 'block_sound()',
 'block_state()',
 'block_tags()',
 'block_tick()',
 'blocks_daylight()',
 'blocks_movement()',
 'create_explosion()',
 'destroy()',
 'effective_light()',
 'emitted_light()',
 'flammable()',
 'generation_status()',
 'hardness()',
 'harvest()',
 'in_slime_chunk()',
 'inhabited_time()',
 'is_chunk_generated()',
 'light()',
 'liquid()',
 'loaded()',
 'loaded_ep()',
 'loaded_status()',
 'map_colour()',
 'material()',
 'opacity()',
 'place_item()',
 'plop()',
 'poi()',
 'pos()',
 'pos_offset()',
 'power()',
 'property()',
 'random_tick()',
 'reload_chunk()',
 'reset_chunk()',
 'sample_noise()',
 'see_sky()',
 'set()',
 'set_biome()',
 'set_poi()',
 'set_structure()',
 'sky_light()',
 'solid()',
 'spawn_potential()',
 'structure_eligibility()',
 'structure_references()',
 'structures()',
 'suffocates()',
 'ticks_randomly()',
 'top()',
 'transparent()',
 'update()',
 'weather()',
 'without_updates()'
  },

'block_iterations': {
 'diamond()',
 'neighbours()',
 'rect()',
 'scan()',
 'volume()'
  },

'entities': {
 'entity_area()',
 'entity_event()',
 'entity_id()',
 'entity_list()',
 'entity_load_handler()',
 'entity_selector()',
 'entity_types()',
 'modify()',
 'player()',
 'query()',
 'spawn()'
  },

'inventories': {
 'close_screen()',
 'crafting_remaining_item()',
 'create_screen()',
 'drop_item()',
 'inventory_find()',
 'inventory_get()',
 'inventory_has_items()',
 'inventory_remove()',
 'inventory_set()',
 'inventory_size()',
 'item_category()',
 'item_list()',
 'item_tags()',
 'recipe_data()',
 'screen_property()',
 'stack_limit()'
 },

'events': {
 '__on_carpet_rule_changes()',
 '__on_chunk_generated()',
 '__on_chunk_loaded()',
 '__on_chunk_unloaded()',
 '__on_close()',
 '__on_explosion()',
 '__on_explosion_outcome()',
 '__on_lightning()',
 '__on_player_attacks_entity()',
 '__on_player_breaks_block()',
 '__on_player_changes_dimension()',
 '__on_player_chooses_recipe()',
 '__on_player_clicks_block()',
 '__on_player_collides_with_entity()',
 '__on_player_command()',
 '__on_player_connects()',
 '__on_player_deals_damage()',
 '__on_player_deploys_elytra()',
 '__on_player_dies()',
 '__on_player_disconnects()',
 '__on_player_drops_item()',
 '__on_player_drops_stack()',
 '__on_player_escapes_sleep()',
 '__on_player_finishes_using_item()',
 '__on_player_interacts_with_block()',
 '__on_player_interacts_with_entity()',
 '__on_player_jumps()',
 '__on_player_message()',
 '__on_player_picks_up_item()',
 '__on_player_places_block()',
 '__on_player_placing_block()',
 '__on_player_releases_item()',
 '__on_player_respawns()',
 '__on_player_rides()',
 '__on_player_right_clicks_block()',
 '__on_player_starts_sneaking()',
 '__on_player_starts_sprinting()',
 '__on_player_stops_sneaking()',
 '__on_player_stops_sprinting()',
 '__on_player_swaps_hands()',
 '__on_player_swings_hand()',
 '__on_player_switches_slot()',
 '__on_player_takes_damage()',
 '__on_player_trades()',
 '__on_player_uses_item()',
 '__on_player_wakes_up()',
 '__on_server_shuts_down()',
 '__on_server_starts()',
 '__on_start()',
 '__on_statistic()',
 '__on_tick()',
 '__on_tick_ender()',
 '__on_tick_nether()',
 'entity_load_handler()',
 'handle_event()',
 'signal_event()'
 },

'scoreboards': {
 'scoreboard()',
 'scoreboard_add()',
 'scoreboard_display()',
 'scoreboard_property()',
 'scoreboard_remove()',
 'team_add()',
 'team_leave()',
 'team_list()',
 'team_property()',
 'team_remove()',
 'bossbar()',
 },

'auxiliaries': {
 'chunk_tickets()',
 'brightness()',
 'create_datapack()',
 'create_marker()',
 'current_dimension()',
 'day_time()',
 'delete_file()',
 'display_title()',
 'draw_shape()',
 'enable_hidden_dimensions()',
 'encode_nbt()',
 'escape_nbt()',
 'format()',
 'game_tick()',
 'get_mob_counts()',
 'in_dimension()',
 'item_display_name()',
 'last_tick_times()',
 'list_files()',
 'load_app_data()',
 'logger()',
 'nbt()',
 'nbt_storage()',
 'parse_nbt()',
 'particle()',
 'particle_box()',
 'particle_line()',
 'read_file()',
 'remove_all_markers()',
 'run()',
 'reset_seed()',
 'save()',
 'schedule()',
 'seed()',
 'sound()',
 'statistic()',
 'store_app_data()',
 'system_info()',
 'tag_matches()',
 'tick_time()',
 'view_distance()',
 'world_time()',
 'write_file()'
 },
}

_not_in_reference = {
 'bossbar()',
 'brightness()',
 'chunk_tickets()',
 'hash_code()',
 'item_category()',
 'long_bits_to_double()',
 'not()',
}

all_functions = set.union(*function_table.values())


tags = {
 ('keyword', 'k', 'Language'): {'print', 'while', 'loop', 'map', 'filter', 'first', 'all', 'c_for', 'for', 'import', 'return', 'exit', 'try', 'throw', 'if', 'break', 'continue', '->', '...'},
 ('type', 't', 'Language'): {'bool', 'number', 'str', 'task', 'm', 'l'},
 ('type', 't', 'Minecraft'): {'block', 'nbt'},
  ('function', 'f', 'Language'): {'reset_seed', 'format', 'logger', 'read_file', 'delete_file', 'write_file', 'list_files', 'load_app_data', 'store_app_data'}
}

all_completions = []
# Variables and Constants
variables = CompletionList(sorted(function_table['variables']),
    default_style={'annotation': 'built-in variable', 'kind': ['variable', 'v', 'Language']})
for p in ('x', 'y', 'z'):
    v = variables[f'_{p}']
    v.kind = ['variable', 'v', 'Minecraft']
    v.details = f'Block {p}-position'
variables['_trace'].kind = ['variable', 'v', 'Minecraft']
variables['_'].details = 'Current element in the collection'
variables['_i'].details = 'Index of the current element'
variables['_a'].details = 'Accumulator variable'

constant = CompletionList(sorted(function_table['constants']),
    default_style={'annotation': 'built-in constant', 'kind': ['navigation', 'c', 'Language']})
constant['euler'].details = 'Euler\'s number e'
constant['pi'].details = 'Archimedes\' constant π'

variables_and_constants = CompletionList.combined(variables, constant, fname=completion_folder/'variables-and-constants.sublime-completions')

all_completions.append(variables_and_constants)

operators = CompletionList(sorted(function_table['operators']),
    default_style={'annotation': 'operator', 'kind': ['function', 'f', 'Language']},
    fname=completion_folder/'operators.sublime-completions')
all_completions.append(operators)

mathematical_functions = CompletionList(sorted(function_table['mathematical_functions']),
    default_style={'annotation': 'mathematical', 'kind': ['function', 'f', 'Language']},
    fname=completion_folder/'mathematical_functions.sublime-completions')
all_completions.append(mathematical_functions)

system_functions = CompletionList(sorted(function_table['system_functions']),
    default_style={'annotation': 'system', 'kind': ['function', 'f', 'Language']},
    fname=completion_folder/'system_functions.sublime-completions')
all_completions.append(system_functions)

loops_and_higher_order_functions = CompletionList(sorted(function_table['loops_and_higher_order_functions']),
    default_style={'annotation': 'iteration', 'kind': ['function', 'f', 'Language']},
    fname=completion_folder/'loops_and_higher_order_functions.sublime-completions')
all_completions.append(loops_and_higher_order_functions)

user_defined_functions_and_program_control_flow = CompletionList(sorted(function_table['user_defined_functions_and_program_control_flow']),
    default_style={'annotation': 'controlflow', 'kind': ['function', 'f', 'Language']},
    fname=completion_folder/'user_defined_functions_and_program_control_flow.sublime-completions')
all_completions.append(user_defined_functions_and_program_control_flow)

container_types = CompletionList(sorted(function_table['container_types']),
    default_style={'annotation': 'container', 'kind': ['function', 'f', 'Language']},
    fname=completion_folder/'container_types.sublime-completions')
all_completions.append(container_types)

app = CompletionList(sorted(function_table['app']),
    default_style={'annotation': 'application', 'kind': ['function', 'f', 'Minecraft']},
    fname=completion_folder/'app.sublime-completions')
all_completions.append(app)

blocks_and_world_access = CompletionList(sorted(function_table['blocks_and_world_access']),
    default_style={'annotation': 'blocks', 'kind': ['function', 'f', 'Minecraft']},
    fname=completion_folder/'blocks_and_world_access.sublime-completions')
all_completions.append(blocks_and_world_access)

block_iterations = CompletionList(sorted(function_table['block_iterations']),
    default_style={'annotation': 'block iteration', 'kind': ['function', 'f', 'Minecraft']},
    fname=completion_folder/'block_iterations.sublime-completions')
all_completions.append(block_iterations)

entities = CompletionList(sorted(function_table['entities']),
    default_style={'annotation': 'entity', 'kind': ['function', 'f', 'Minecraft']},
    fname=completion_folder/'entities.sublime-completions')
all_completions.append(entities)

inventories = CompletionList(sorted(function_table['inventories']),
    default_style={'annotation': 'inventory', 'kind': ['function', 'f', 'Minecraft']},
    fname=completion_folder/'inventories.sublime-completions')
all_completions.append(inventories)

events = CompletionList(sorted(function_table['events']),
    default_style={'annotation': 'event', 'kind': ['function', 'f', 'Minecraft']},
    fname=completion_folder/'events.sublime-completions')
all_completions.append(events)

scoreboards = CompletionList(sorted(function_table['scoreboards']),
    default_style={'annotation': 'scoreboard', 'kind': ['function', 'f', 'Minecraft']},
    fname=completion_folder/'scoreboards.sublime-completions')
all_completions.append(scoreboards)

auxiliaries = CompletionList(sorted(function_table['auxiliaries']),
    default_style={'annotation': 'auxiliary', 'kind': ['function', 'f', 'Minecraft']},
    fname=completion_folder/'auxiliaries.sublime-completions')

all_completions.append(auxiliaries)

for en in all_completions:
    for item in en.items:
        item.contents = item.trigger.replace('()', '($1)')
    for tag, triggers in tags.items():
        tag = list(tag)
        for trigger in triggers:
            try:
                en[trigger+'()'].kind = tag
            except KeyError:
                pass
    en.to_json()