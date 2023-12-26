// $(()=>{
//     $("#article_preview_btn").click(()=>{
//         var converter = new showdown.Converter();
//         var content_html = converter.makeHtml($('#content').val());
//         $('#article_preview').html(content_html)
//     });
// });





$(()=>{
        var converter = new showdown.Converter();
        var target = $('#content')
        target.on('keyup', (event) => {
            var content_html = converter.makeHtml($('#content').val());
            $('#article_preview').html(content_html)
          });
});