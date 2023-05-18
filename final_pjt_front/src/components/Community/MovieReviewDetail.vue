<template>
	<div>
		<h1>Detail</h1>
		<p>글 번호 : {{ review_article?.id }}</p>
		<p>글 제목 : {{ review_article?.title }}</p>
		<p>내용 : {{ review_article?.content }}</p>
		<p>작성시간 : {{ review_article?.created_at }}</p>
		<p>수정시간 : {{ review_article?.updated_at }}</p>
	</div>
</template>

<script>
export default {
	name: "MovieReviewDetail",
	data() {
		return {
			review_article: null,
		}
	}
	// axios로 Django 데이터베이스 서버에 연결 후 작업
}
</script>

<style>

</style>