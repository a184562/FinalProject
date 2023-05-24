<template>
	<div class="selectBoard mt-5">
		<h2 class="genreTitle pt-3 pb-3">선호 장르 선택</h2>
		<div class="genreContainer mt-4 d-flex">
			<div class="align-self-center ps-5 pe-5">
				<button v-for="genre in genre_list" :key="genre.id" :id="genre.id" class="btn btn-lg btn-dark mt-3 ms-3 me-3 mb-3" @click="selectGenres(genre)">{{genre.name}}</button>
			</div>
		</div>
		
		<div v-if="genre.length >= 3" class="d-grid gap-2 mt-3 submitbtn pt-3">
			<input class="btn btn-dark ms-3 me-3" type="submit" @click="genres" value="제출">
		</div>
		<div v-else class="d-grid gap-2 mt-3 submitbtn pt-3">
			<input class="btn btn-dark ms-3 me-3" type="submit" @click="genres" value="제출" disabled>
		</div>
		
	</div>
</template>

<script>
import axios from 'axios'
const Django_API_URL = 'http://127.0.0.1:8000'


export default {
	name: 'GenreSelect',
	data() {
		return {
			genre_list : null,
			genre :[],
		}
	},
	created() {
		axios({
			method: 'get',
			url: `${Django_API_URL}/api/v1/movie/genres/`,
		})
		.then((res) => {
			console.log(res)
			this.genre_list = res.data
		})
		.catch((err) => console.log(err))
	},
	methods:{
		selectGenres(genre) {
			let genre_HTML = document.getElementById(genre.id)
			if(this.genre.indexOf(genre.id) === -1) {
				this.genre.push(genre.id)
				genre_HTML.className = "btn btn-lg btn-secondary mt-3 ms-3 me-3 mb-3"
			}
			else {
				for(let i = 0; i < this.genre.length; i++) {
					if(this.genre[i] === genre.id) {
						this.genre.splice(i, 1)
						i--
						genre_HTML.className = "btn btn-lg btn-dark mt-3 ms-3 me-3 mb-3"
					}
				}
				
			}
			console.log(this.genre)
		},
		genres(){
			const genre = this.genre
			if(genre.length > 5) {
				alert("너무 많이 선택하셨습니다. 5개 이하로 선택해주세요.")
			}
			else {
				axios({
				method:'post',
				url : 'http://127.0.0.1:8000/api/v1/usergenre/',
				data:{
					genre
				},
				headers:{
					Authorization : `Token ${this.$store.state.token}`					
				}
			})
			.then(()=>{
				this.$router.push({name:'movies'})
			})
			.catch(()=>{})
			}
			
		}
	}
}
</script>

<style scoped>
.genreTitle {
	border-bottom: solid grey 1px;
}
.selectBoard {
	border-radius: 0.5rem;
	width: 65%;
	height: 70%;
	margin: auto;
	box-shadow: 4px 4px 4px grey;
	background-color: #141414;
}
.genreContainer {
	width: 80%;
	height: 70%;
	border-radius: .5rem;
	margin: auto;
}
.submitbtn {
	
	border-top: solid grey 1px;
}
.temp {
	margin: auto;
}
</style>