FROM continuumio/miniconda

RUN apt-get update --fix-missing  && apt-get install -y r-base && apt-get clean && rm -rf /var/lib/apt/lists/*

ADD environment.yml /tmp/environment.yml
RUN conda env create -f /tmp/environment.yml

RUN Rscript -e 'install.packages(c("IRkernel","lme4"),repos="https://cran.rstudio.com")'
RUN /bin/bash -c "source activate gwas-lecture && Rscript -e 'IRkernel::installspec()'"

# Pull the environment name out of the environment.yml
RUN echo "source activate $(head -1 /tmp/environment.yml | cut -d' ' -f2)" > ~/.bashrc
ENV PATH /opt/conda/envs/$(head -1 /tmp/environment.yml | cut -d' ' -f2)/bin:$PATH

RUN mkdir /root/gwas-lecture
COPY . /root/gwas-lecture

EXPOSE 8888
CMD ["/opt/conda/envs/gwas-lecture/bin/jupyter", "notebook", "--ip='0.0.0.0'","--allow-root","--port","8888","--no-browser","--notebook-dir","/root/gwas-lecture/"]