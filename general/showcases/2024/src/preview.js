import { projects } from "../data.mjs";

const params = new URLSearchParams(window.location.search);

const projectId = params.get("project-id");

if (projectId) {
    const project = projects.find(project => project.id === projectId);

    const wrapper = document.querySelector(".c-ibnQYQ");

    const _index = (project.position.toString().padStart(2, '0'));

    if (wrapper) {
        const content = `
            <div class="c-djYynj">
                <nav class="c-kwlaUE">
                    <div class="c-bZNrxE c-bZNrxE-dwGeto-state-default">
                        <a href="/">${project.type === "Projeto" ? "Projetos" : "Jogos"}</a>
                    </div>

                    <img alt="" loading="lazy" width="6" height="10.5" decoding="async" data-nimg="1" src="https://www.rocketseat.com.br/boracodar/icons/arrow-right.svg" style="color: transparent;" />
                    
                    <div class="c-bZNrxE c-bZNrxE-cJbzxd-state-active">
                        <span>${project.type} #${_index}</span>
                    </div>
                </nav>
            </div>

            <section class="c-fNFMJl">
                <div class="c-djYynj">
                    <div class="c-ldPVcj">
                        <div class="c-jzHPju">
                            <div class="c-hfgNXw">
                                <strong>${project.type} #${_index}</strong>
                            </div>
                        </div>
                        
                        <header class="c-dezZDU">
                            <h1 class="c-gGZtOO">${project.name}</h1>
                            <p>${project.description}</p>
                        </header>
                        
                        <a data-id="cta-watch-resolution" href="${project.url}" target="_blank" rel="noopener noreferrer" class="c-kkZDxd c-kkZDxd-DDgKx-type-secondary">Acessar resultado</a>
                        
                        <footer class="c-fHigTs">Os ${project.type === "Projeto" ? "projetos" : "jogos"} foram desenvolvidos por alunos da faculdade, podendo ter sido feitos durante o curso ou de forma independente.
                        </footer>
                    </div>
                </div>

                ${project.url.includes("youtube") ? 
                    `<iframe data-id="project-image" width="592" height="340.23" src="${project.url}" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>` 
                    : project.url.includes(".webm") ? 
                    `<video controls width="592" height="340.23">
                        <source src="${project.url}" type="video/webm">
                        Seu navegador não suporta o elemento <code>video</code>.
                     </video>` 
                    : 
                    `<img alt="" src="${project.coverUrl}" data-id="project-image" width="592" height="340.23" decoding="async" data-nimg="1" style="color: transparent; animation: 1s linear 0s 1 normal none running k-feVUdh;">`
                }
            </section>
        `;

        wrapper.innerHTML = content;
    }

    document.title = `${project.name} | X Mostra de Profissões - FEPI 2024`;
}