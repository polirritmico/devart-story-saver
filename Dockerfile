FROM python

ARG USER=docker_user

RUN useradd -ms /bin/bash ${USER}

ENV PATH="${PATH}:/home/${USER}/devart-story-saver"

WORKDIR /home/${USER}/devart-story-saver

RUN chown -R ${USER}:${USER}

USER ${USER}

COPY --chown=${USER} . ./

RUN python -m pip install -r requirements.txt

