from flask import Flask, render_template_string

app = Flask(__name__)

@app.route('/')
def home():
    playlist_id = "3OWztfsk062tnMifJTjcxR"
    html_embed = f"""
    <iframe
        title="Spotify Embed: Recommendation Playlist"
        src="https://open.spotify.com/embed/playlist/{playlist_id}?utm_source=generator&theme=0"
        width="100%"
        height="100%"
        style="min-height: 360px;"
        frameborder="0"
        allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture"
        loading="lazy">
    </iframe>
    """
    return render_template_string(html_embed)

if __name__ == '__main__':
    app.run(debug=True)
