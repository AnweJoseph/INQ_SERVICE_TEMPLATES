from jinja2 import Environment, FileSystemLoader, StrictUndefined
import yaml

def processing_vrf():
    config = yaml.full_load(open('./vrf_data.yaml'))
    
    env = Environment(loader = FileSystemLoader('.'), trim_blocks=True)
    template = env.get_template('vrf_template.j2')
    output = template.render(config)

    save_template = open('processed_vrf', 'w')
    save_template.write(output)
    save_template.close
