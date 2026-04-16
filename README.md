# blog

Welcome to my personal mind dump :)

## Testing

### Local Host
```
cd ~/blog/src/webapp
source /home/david/venv/bin/activate
flask --app ./api/controller.py run --debug
```

### Vercel Test
```
cd ~/blog/src/webapp
vercel deploy
```

## Deployment

Pushing to mainline will automatically deploy to prod. 
This will cause main page to throw 404.
You need to deploy via vercel.

```
cd ~/blog/src/webapp
vercel --prod
```

