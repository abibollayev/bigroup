class ApiService {
	constructor(baseURL) {
		this.baseURL = baseURL
	}

	async fetchData(endpoint) {
		try {
			const response = await fetch(`${this.baseURL}${endpoint}`)
			if (!response.ok) {
				throw new Error(`HTTP Error: ${response.status}`)
			}
			return await response.json()
		} catch (error) {
			console.error('Fetch error:', error)
			return null
		}
	}
}

class Component {
	constructor(selector) {
		this.container = document.querySelector(selector)
		if (!this.container) {
			throw new Error(`Element with selector "${selector}" not found.`)
		}
	}

	render(html) {
		this.container.innerHTML = html
	}
}

class DataListComponent extends Component {
	constructor(selector) {
		super(selector)
	}

	renderDataList(data) {
		const html = data
			.map(
				item => `
				<a href="/projects/${item.id}" class="project__item">
					<img src="http://localhost:8000/media/${item.main_img}" />
					<div class="project__item-type ${item.type == 'Бизнес' ? 'business' : ''}">
						${item.type}
					</div>
					<p class="project__item-title">${item.title}</p>
					<p class="project__item-price">${item.price}</p>
					<p class="project__item-count">
						${item.apartment_count} квартир <span>в продаже</span>
					</p>
				</a>`
			)
			.join('')
		this.render(html)
	}
}

class App {
	#data

	constructor(apiService, dataComponent) {
		this.apiService = apiService
		this.dataComponent = dataComponent
	}

	async init() {
		this.#data = await this.apiService.fetchData('/projects/items')
		if (this.#data) {
			this.dataComponent.renderDataList(this.#data)
		}
	}

	filter(cb) {
		const newData = this.#data.filter(cb)
		this.dataComponent.renderDataList(newData)
	}
}

const apiService = new ApiService('http://127.0.0.1:8000')
const dataComponent = new DataListComponent('#project-list')

const app = new App(apiService, dataComponent)
app.init()
projectFilter(app)

function projectFilter(app) {
	const cityFilter = city => {
		return item => item.city === city
	}

	const filter = document.getElementById('project-filter')
	const filterPopup = document.getElementById('project-filter-popup')
	const astanaBtn = document.getElementById('project-filter-astana')
	const almatyBtn = document.getElementById('project-filter-almaty')

	filter.addEventListener('click', () => {
		filterPopup.classList.toggle('active')
	})

	astanaBtn.addEventListener('click', () => {
		filterPopup.classList.remove('active')
		app.filter(cityFilter('Астана'))
	})

	almatyBtn.addEventListener('click', () => {
		filterPopup.classList.remove('active')
		app.filter(cityFilter('Алматы'))
	})
}
