from model.acticle import Article


class TestArticleModel(object):

    def test_make_user(self, user):
        article = Article(
            title="제목입니다.",
            author=user,
            slug="",
            body="내용입니다.",
            discription=""
        )

        assert article.title == "제목입니다."
        assert article.body == "내용입니다."
        assert article.author is user

    def test_save_artcle(self, user, session):
        article = Article(
            title="제목입니다.",
            author=user,
            slug="",
            body="내용입니다.",
            discription=""
        )

        session.add(article)


    def test_find_article(self, session, user):
        article = Article(
            title="제목입니다.",
            author=user,
            slug="",
            body="내용입니다.",
            discription=""
        )

        session.add(article)
        found_acticle = session.query(Article).first()

        assert article is found_acticle


    def test_to_dict(self, user, session):
        article = Article(
            title="제목입니다.",
            author=user,
            slug="",
            body="내용입니다.",
            discription=""
        )

        session.add(article)
        session.commit()

        article_dict = article.to_dict()
        assert "createdAt" in article_dict