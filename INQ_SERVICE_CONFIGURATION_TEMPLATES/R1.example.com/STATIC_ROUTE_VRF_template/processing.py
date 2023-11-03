from jinja2 import Environment, FileSystemLoader, StrictUndefined
import yaml

def processing_static():
    config = yaml.full_load(open('./static_route_data.yaml'))
    
    env = Environment(loader = FileSystemLoader('.'), trim_blocks=True)
    template = env.get_template('static_route_template.j2')
    output = template.render(config)

    save_template = open('processed_static', 'w')
    save_template.write(output)
    save_template.close

