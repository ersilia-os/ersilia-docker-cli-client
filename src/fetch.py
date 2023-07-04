import subprocess


class ModelFetcher(object):
    def __init__(self, model_id):
        self.model_id = model_id
        self.image_name = "ersiliaos/" + model_id + ":latest"
        self.container_name = "ersilia_shell"

    def run(self):
        subprocess.Popen(
            'docker exec -it {0} bash -c "ersilia -v fetch {1} --from_dockerhub --reuse"'.format(
                self.container_name, self.model_id
            ),
            shell=True,
        ).wait()
