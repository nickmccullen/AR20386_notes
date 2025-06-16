import matplotlib.pyplot as plt
import numpy as np

np.random.seed(42)

N=5

mat=np.zeros((N+2,N+2))
mat[1:N+1,1:N+1]=30*np.random.random((N,N))

plt.rc("font", size=20)
fig=plt.figure(figsize=(12,6))
ax=fig.add_subplot(121)

cax = ax.imshow(mat[1:N+1,1:N+1], cmap=plt.get_cmap("gist_heat_r"), interpolation="nearest", origin="lower")

ax.set_xlabel("Coordinate $x$")
ax.set_ylabel("Coordinate $y$")

for j in range(N):
    for i in range(N):
        ax.text(i-0.2, j-0.2, "{:.0f}".format(mat[j+1,i+1]))
        
fig.colorbar(cax)  

ax2=fig.add_subplot(122)
cax2 = ax2.imshow(mat[1:N+1,1:N+1], origin="lower", cmap=plt.get_cmap("gist_heat_r"))#, interpolation="nearest", origin="lower")

ax2.set_xlabel("Coordinate $x$")
ax2.set_ylabel("Coordinate $y$")
ax2.set_title(r"Heat Flow $\vec{q}=- k \vec{V}$")

k=0.02

for j in range(1,N+1):
    for i in range(1,N+1):
        flowX=k*(mat[j,i]-mat[j,i+1])
        flowY=k*(mat[j,i]-mat[j+1,i])
        if j<=N:
            ax2.arrow(i-0.5-flowX/2, j-1, flowX, 0, head_width=0.1, width=0.02, color="blue")
        if i<=N:
            ax2.arrow(i-1, j-0.5-flowY/2, 0, flowY, head_width=0.1, width=0.02, color="blue")

fig.colorbar(cax, label="Temperature $T$ $(^{\circ}C)$")

fig.savefig("temps1.png")
