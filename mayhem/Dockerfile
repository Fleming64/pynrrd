FROM python:3.8-bullseye
RUN pip3 install atheris

COPY . /pynrrd
WORKDIR /pynrrd
RUN python3 -m pip install . && chmod +x fuzz/pynrrd_fuzz.py

ENTRYPOINT [ ]
CMD ["/pynrrd/fuzz/pynrrd_fuzz.py"]