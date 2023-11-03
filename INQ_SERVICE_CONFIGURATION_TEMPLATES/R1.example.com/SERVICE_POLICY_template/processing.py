from jinja2 import Environment, FileSystemLoader, StrictUndefined
import yaml

def processing_policy():
    config = yaml.full_load(open('./policy_data.yaml'))
    
    env = Environment(loader = FileSystemLoader('.'), trim_blocks=True)
    template = env.get_template('policy_template.j2')
    output = template.render(config)

    save_template = open('processed_policy', 'w')
    save_template.write(output)
    save_template.close

