from jinja2 import Environment, FileSystemLoader, StrictUndefined
import yaml

def processing_bgp():
    config = yaml.full_load(open('./bgp_ipv4_data.yaml'))
    
    env = Environment(loader = FileSystemLoader('.'), trim_blocks=True)
    template = env.get_template('bgp_template.j2')
    output = template.render(config)

    save_template = open('processed_bgp', 'w')
    save_template.write(output)
    save_template.close

