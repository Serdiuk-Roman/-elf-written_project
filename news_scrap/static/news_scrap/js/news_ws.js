
var news_ws = new WebSocket(
  'ws://' + window.location.host + '/ws/'
);

function addNews(news_list) {
  for (el in news_list) {
    var post = `
    <div class="card">
      <div class="card-header">
        <p>` + news_list[el].post_title + `</p>
      </div>
      <div class="card-body">
      <a href="` + news_list[el].link_url + `" class="btn btn-secondary btn-sm" >source</a>
       <span>` + news_list[el].time + `</span>
       <p>` + news_list[el].short_text + `</p>
      </div>

      <form>
        <input id="btn` + el + `" type="button" value="quick show + db" class="btn btn-secondary btn-sm">
      </form>

      <script>
        $('#btn` + el + `').click(function(){
            $.ajax({
                url: "/create/",
                cache: false,
                data: "news_url=` + news_list[el].link_url + `",
            });
        });
      <\/script>

    </div>`;
    $('#news').append(post);
  }
}

function addPost(news_post) {
  var post = `
    <div class="card">
      <div class="card-header">
        <p>` + news_post.post_title + `</p>
      </div>
      <div class="card-body">
        <a href="` + news_post.news_link + `" class="btn btn-secondary btn-sm" >source</a>
        <p>` + news_post.post_datetime + `</p>
        <p>` + news_post.full_text + `</p>
      </div>
    </div>`;
  $('#best_post').append(post);
}

news_ws.onmessage = function(event_) {
  var message = JSON.parse(event_.data)

  switch(message.type) {
    case "single":
      var news_post = message.best_post;
      document.querySelector('#best_post').innerHTML = '';
      addPost(news_post);
      break;
    case "list":
      var news_list = message['news_list'];
      document.querySelector('#news').innerHTML = '';
      addNews(news_list);
      break;
  }
}

news_ws.onclose = function(e) {
  console.error('News socket closed')
}
