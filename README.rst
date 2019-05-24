invoker-k8s
===========

An invoker app for maintaining and interacting with kubernetes. It assumes
kustomize is being used for building the kubernetes config.

Assumptions
-----------

We assume ``kustomize`` is being used for handling kubernetes configuration.


Commands
--------

* ``<env>.k8s.config``: Configures ``kubectl`` to interact with the given
  cluster with the correct namespace.
* ``<env>.k8s.apply``: Builds and applies the ``kustomize`` configuration.
* ``<env>.k8s.deploy``: Updates the kubernetes deployment with the new image.
* ``<env>.k8s.kustomize``: Builds and writes the ``kustomize`` config to
  stdout or a file.

Parameters
----------

* ``kubectl_config_path``: The module path used for configuring ``kubectl``
  for your cluster (default: ``invoker_k8s.configure.default``)
* ``kubectl_exe``: The command to use for interacting with the kubernetes
  cluster (default ``kubectl``)
* ``kubectl_context``: The name of the context to use during configuration.
* ``kubectl_namespace``: The namespace to use during configuration.
* ``kubectl_cluster``: The name of the cluster.
* ``kubectl_user``: The name of the user to use for interacting with the
  cluster (from your local kubernetes config)
* ``kustomize_cmd``: The command to use for building the kustomize config
  (default: ``kustomize``)
* ``kustomize_root``: The path to the root of the kustomize configuration
  (default: ``k8s``)
* ``kustomize_path``: The path to the kustomize overlay for the environment
  relative to the ``kustomize_root`` (default: ``overlays/<env>``).
* ``kustomize_deploy_images``: The names of the images to deploy
