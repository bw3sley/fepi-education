import { projects } from "./data.mjs";

for (const project of projects) {
    const wrapper = document.querySelector(".c-fzRajX");

    const _index = (project.position.toString().padStart(2, '0'));

    const item = `
        <div class="c-hJHZEu">
            <a href="./preview.html?project-id=${project.id}">
                <img alt="" src="${project.coverUrl}" data-id="project-image" width="592" height="340.23" decoding="async" data-nimg="${project.id}" style="color: transparent; animation: 1s linear 0s 1 normal none running k-feVUdh;" />
                
                <div class="c-dhaRcH">
                    <div class="c-ioaeHt">
                        <div class="c-hfgNXw">
                            <strong>${project.type} #${_index}</strong>
                        </div>
                    </div>
                    
                    <header class="c-gAFhlW">
                        <h1 class="c-gEOLIN">${project.name}</h1>

                        <p>${project.description}</p>
                    </header>
                </div>
            </a>
        </div>
    `;

    wrapper.innerHTML += item;
}

const tabs = document.querySelectorAll(".c-WzmVl");
const indicator = document.querySelector(".c-jbjKZJ");

const mainProject = document.querySelector(".c-cpyHAE");
const sideProjects = document.querySelector(".c-fzRajX");

const courses = document.querySelector(".c-slakfg");

for (const tab of tabs) {
    tab.addEventListener("click", (event) => {
        event.preventDefault();

        document.querySelector(".c-WzmVl-gdCQzR-state-active")?.classList.remove("c-WzmVl-gdCQzR-state-active");
        document.querySelector("[data-active='true']")?.setAttribute("data-active", "false");

        tab.classList.add("c-WzmVl-gdCQzR-state-active");
        tab.setAttribute("data-active", "true");

        if (indicator) {
            indicator.style.width = `${tab.offsetWidth}px`;
            indicator.style.transform = `translateX(${tab.offsetLeft}px)`;
        }

        if (tab.textContent.trim() === "Os cursos") {
            mainProject.style.display = "none";
            sideProjects.style.display = "none";

            courses.style.display = "flex";
        }

        else {
            mainProject.style.display = "flex";
            sideProjects.style.display = "grid";

            courses.style.display = "none";
        }
    })
}