from jinja2 import Environment, FileSystemLoader, StrictUndefined
import yaml

def processing_interface():
    config = yaml.full_load(open('./interface_data.yaml'))
    
    env = Environment(loader = FileSystemLoader('.'), trim_blocks=True)
    template = env.get_template('interface_template.j2')
    output = template.render(config)

    save_template = open('processed_interface', 'w')
    save_template.write(output)
    save_template.close

